%global packname  TwoStepCLogit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Conditional logistic regression: A two-step estimation method

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Conditional logistic regression with longitudinal follow up and
individual-level random coefficients: A stable and efficient two-step
estimation method

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
%doc %{rlibdir}/TwoStepCLogit/DESCRIPTION
%doc %{rlibdir}/TwoStepCLogit/html
%{rlibdir}/TwoStepCLogit/INDEX
%{rlibdir}/TwoStepCLogit/data
%{rlibdir}/TwoStepCLogit/R
%{rlibdir}/TwoStepCLogit/NAMESPACE
%{rlibdir}/TwoStepCLogit/help
%{rlibdir}/TwoStepCLogit/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora