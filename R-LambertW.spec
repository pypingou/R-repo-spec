%global packname  LambertW
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.9.5
Release:          1%{?dist}
Summary:          Gaussianize and analyze skewed, heavy-tailed data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-moments R-gsl R-MASS R-nortest R-maxLik 


BuildRequires:    R-devel tex(latex) R-moments R-gsl R-MASS R-nortest R-maxLik



%description
The Lambert W framework is a new generalized way to analyze skewed,
heavy-tailed data. Lambert W random variables (RV) are based on an
input/output framework where the input is a RV X with distribution F(x),
and the output Y = func(X) has similar properties as X (but slightly
skewed or heavy-tailed). Then this transformed RV Y has a Lambert W x F
distribution - for details see References. This package contains functions
to perform a Lambert W analysis of skewed and heavy-tailed data: data can
be simulated, parameters can be estimated from real world data, quantiles
can be computed, and results plotted/printed in a 'nice' way. Probably the
most important function is 'Gaussianize', which works the same way as the
R function 'scale' but actually makes your data Gaussian. An optional
modular toolkit implementation allows users to define their own Lambert W
x 'my favorite distribution' and use it for their analysis.

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.9.5-1
- initial package for Fedora