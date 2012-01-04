%global packname  eha
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          Event History Analysis

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics R-utils R-survival 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-utils R-survival 

%description
Event history analysis: Sampling of risk sets in Cox regression,
selections in the Lexis diagram, bootstrapping. Parametric proportional
hazards fitting with left truncation and right censoring for common
families of distributions, piecewise constant hazards, and discrete
models. AFT regression for left truncated and right censored data. Binary
and Poisson regression for clustered data, fixed and random effects with

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
%doc %{rlibdir}/eha/doc
%doc %{rlibdir}/eha/html
%doc %{rlibdir}/eha/DESCRIPTION
%{rlibdir}/eha/libs
%{rlibdir}/eha/help
%{rlibdir}/eha/Meta
%{rlibdir}/eha/data
%{rlibdir}/eha/INDEX
%{rlibdir}/eha/R
%{rlibdir}/eha/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.5-1
- initial package for Fedora