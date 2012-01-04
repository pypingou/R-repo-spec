%global packname  SMVar
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          Structural Model for variances

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Implements the structural model for variances in order to detect
differentially expressed genes from gene expression data

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
%doc %{rlibdir}/SMVar/html
%doc %{rlibdir}/SMVar/DESCRIPTION
%{rlibdir}/SMVar/help
%{rlibdir}/SMVar/R
%{rlibdir}/SMVar/INDEX
%{rlibdir}/SMVar/NAMESPACE
%{rlibdir}/SMVar/data
%{rlibdir}/SMVar/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.3-1
- initial package for Fedora