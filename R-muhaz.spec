%global packname  muhaz
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          Hazard Function Estimation in Survival Analysis

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A package for producing a smooth estimate of the hazard function for
censored data.

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
%doc %{rlibdir}/muhaz/DESCRIPTION
%doc %{rlibdir}/muhaz/html
%{rlibdir}/muhaz/NAMESPACE
%{rlibdir}/muhaz/help
%{rlibdir}/muhaz/INDEX
%{rlibdir}/muhaz/Meta
%{rlibdir}/muhaz/R
%{rlibdir}/muhaz/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.5-1
- initial package for Fedora