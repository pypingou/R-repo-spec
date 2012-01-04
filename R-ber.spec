%global packname  ber
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Batch Effects Removal

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The functions in this package remove batch effects from microarrary
normalized data. The expression levels of the genes are represented in a
matrix where rows correspond to independent samples and columns to genes
(variables). The batches are represented by categorical variables (objects
of class factor). When further covariates of interest are available they
can be used to remove efficiently the batch effects and adjust the data.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/ber/DESCRIPTION
%doc %{rlibdir}/ber/html
%{rlibdir}/ber/R
%{rlibdir}/ber/help
%{rlibdir}/ber/INDEX
%{rlibdir}/ber/Meta

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora