%global packname  TwoWaySurvival
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Additiv Two-Way Hazards Modelling of Right Censored Survival Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines 

BuildRequires:    R-devel tex(latex) R-splines 

%description
The package offers a fitting of smooth varying coefficients in an additiv
two-way hazard model. A one-way hazard model can also be fittied with
supplementary functions. Nonparametric penalized spline (p-spline) fitting
is proposed. In the two-way case two alternativ models can be analized: In
the first one a non periodic calendar time, like the calendar year, is
considered as a second time scale (additionaly to the survival time), and
as a spline basis truncated polynomial functions are chosen. In the second
model a periodic time scale, like a season of year, is additionaly
considered, and as a spline basis the b-splines are selected. In the
one-way case the user can choose between these two alternative penalized

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
%doc %{rlibdir}/TwoWaySurvival/doc
%doc %{rlibdir}/TwoWaySurvival/DESCRIPTION
%doc %{rlibdir}/TwoWaySurvival/html
%{rlibdir}/TwoWaySurvival/INDEX
%{rlibdir}/TwoWaySurvival/NAMESPACE
%{rlibdir}/TwoWaySurvival/data
%{rlibdir}/TwoWaySurvival/R
%{rlibdir}/TwoWaySurvival/help
%{rlibdir}/TwoWaySurvival/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora