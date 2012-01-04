%global packname  mstate
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          Data preparation, estimation and prediction in multi-state models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Functions for data preparation, descriptives, hazard estimation and
prediction with Aalen-Johansen or simulation in competing risks and
multi-state models

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
%doc %{rlibdir}/mstate/html
%doc %{rlibdir}/mstate/DESCRIPTION
%doc %{rlibdir}/mstate/doc
%doc %{rlibdir}/mstate/CITATION
%{rlibdir}/mstate/help
%{rlibdir}/mstate/libs
%{rlibdir}/mstate/Meta
%{rlibdir}/mstate/data
%{rlibdir}/mstate/R
%{rlibdir}/mstate/NAMESPACE
%{rlibdir}/mstate/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.6-1
- initial package for Fedora