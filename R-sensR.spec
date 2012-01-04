%global packname  sensR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.13
Release:          1%{?dist}
Summary:          Thurstonian models for sensory discrimination

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ordinal R-numDeriv 


BuildRequires:    R-devel tex(latex) R-ordinal R-numDeriv



%description
Provides methods for sensory discrimination methods; duotrio, triangle,
2-AFC, 3-AFC, A-not A, same-different and 2-AC.  This enables the
calculation of d-primes, standard errors of d-primes, sample size and
power computations, and comparisons of different d-primes. Methods for
profile likelihood confidence intervals and plotting are included.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.13-1
- initial package for Fedora