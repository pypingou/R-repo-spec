%global packname  TwoPhaseInd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Two-Phase Independence

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Semiparametric Estimation Exploiting Covariate Independence in Two-Phase
Randomized Trials

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
%doc %{rlibdir}/TwoPhaseInd/doc
%doc %{rlibdir}/TwoPhaseInd/html
%doc %{rlibdir}/TwoPhaseInd/DESCRIPTION
%{rlibdir}/TwoPhaseInd/libs
RPM build errors:
%{rlibdir}/TwoPhaseInd/R
%{rlibdir}/TwoPhaseInd/NAMESPACE
%{rlibdir}/TwoPhaseInd/INDEX
%{rlibdir}/TwoPhaseInd/Meta
%{rlibdir}/TwoPhaseInd/help
%{rlibdir}/TwoPhaseInd/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora