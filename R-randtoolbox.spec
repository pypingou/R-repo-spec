%global packname  randtoolbox
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10
Release:          1%{?dist}
Summary:          toolbox for pseudo and quasi random number generation and RNG tests.

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rngWELL 

BuildRequires:    R-devel tex(latex) R-rngWELL 

%description
The package provides (1) pseudo random generators - general linear
congruential generators (Park Miller) and multiple recursive generators
(Knuth TAOCP), generalized feedback shift register (SF-Mersenne Twister
algorithm and WELL generators); (2) quasi random generators - the Torus
algorithm, the Sobol sequence, the Halton sequence (thus include Van der
Corput sequence) and (3) some additional tests such as the gap test, the
serial test, the poker test... The package depends on rngWELL package but
it can be provided without this dependency on demand to the maintainer.
For true random number generation, use the 'random' package, for Latin
Hypercube Sampling (a hybrid QMC method), use the 'lhs' package, a number
of RNGs and tests for RNGs are provided by 'RDieHarder', all available on
CRAN. There is also a small stand-alone package 'rngwell19937' for the
WELL19937a RNG.

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
%doc %{rlibdir}/randtoolbox/DESCRIPTION
%doc %{rlibdir}/randtoolbox/doc
%doc %{rlibdir}/randtoolbox/CITATION
%doc %{rlibdir}/randtoolbox/NEWS
%doc %{rlibdir}/randtoolbox/LICENCE
%doc %{rlibdir}/randtoolbox/html
%{rlibdir}/randtoolbox/NAMESPACE
%{rlibdir}/randtoolbox/help
%{rlibdir}/randtoolbox/INDEX
%{rlibdir}/randtoolbox/DocCopying.pdf
%{rlibdir}/randtoolbox/R
%{rlibdir}/randtoolbox/Meta
%{rlibdir}/randtoolbox/libs

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10-1
- initial package for Fedora