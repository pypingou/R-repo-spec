%global packname  pcse
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8
Release:          1%{?dist}
Summary:          Panel-Corrected Standard Error Estimation in R

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains a function to estimate panel-corrected standard
errors. Data may contain balanced or unbalanced panels.

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
%doc %{rlibdir}/pcse/doc
%doc %{rlibdir}/pcse/CITATION
%doc %{rlibdir}/pcse/DESCRIPTION
%doc %{rlibdir}/pcse/html
%{rlibdir}/pcse/LICENSE
%{rlibdir}/pcse/Meta
%{rlibdir}/pcse/demo
%{rlibdir}/pcse/NAMESPACE
%{rlibdir}/pcse/R
%{rlibdir}/pcse/data
%{rlibdir}/pcse/help
%{rlibdir}/pcse/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8-1
- initial package for Fedora