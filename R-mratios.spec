%global packname  mratios
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.16
Release:          1%{?dist}
Summary:          Inferences for ratios of coefficients in the general linear model

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-mvtnorm 


%description
With this package, it is possible to perform (simultaneous) inferences for
ratios of linear combinations of coefficients in the general linear model.
In particular, tests and confidence interval estimations for ratios of
treatment means in the normal one-way layout and confidence interval
estimations like in (multiple) slope ratio and parallel line assays can be
carried out. Moreover, it is possible to calculate the sample sizes
required in comparisons with a control based on relative margins. For the
simple two-sample problem, functions for a t-test for ratio-formatted
hypotheses and the corresponding Fieller-type confidence interval are
provided assuming homogeneous or heterogeneous group variances.

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
%doc %{rlibdir}/mratios/html
%doc %{rlibdir}/mratios/DESCRIPTION
%{rlibdir}/mratios/R
%{rlibdir}/mratios/NAMESPACE
%{rlibdir}/mratios/INDEX
%{rlibdir}/mratios/help
%{rlibdir}/mratios/data
%{rlibdir}/mratios/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.16-1
- initial package for Fedora