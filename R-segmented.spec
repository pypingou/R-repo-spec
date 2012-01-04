%global packname  segmented
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.8.2
Release:          1%{?dist}
Summary:          Segmented relationships in regression models

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-8.2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Given a (generalized) linear model, segmented `updates' the model by
adding one or more segmented relationships. Several variables with
multiple breakpoints are allowed.

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
%doc %{rlibdir}/segmented/CITATION
%doc %{rlibdir}/segmented/NEWS
%doc %{rlibdir}/segmented/html
%doc %{rlibdir}/segmented/DESCRIPTION
%{rlibdir}/segmented/Meta
%{rlibdir}/segmented/help
%{rlibdir}/segmented/R
%{rlibdir}/segmented/INDEX
%{rlibdir}/segmented/data
%{rlibdir}/segmented/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.8.2-1
- initial package for Fedora