%global packname  gcbd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          GPU/CPU Benchmarking in Debian-based systems

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RSQLite R-plyr R-reshape R-lattice 


BuildRequires:    R-devel tex(latex) R-RSQLite R-plyr R-reshape R-lattice



%description
GPU/CPU Benchmarking on Debian-package based systems This package
benchmarks performance of a few standard linear algebra operations (such
as a matrix product and QR, SVD and LU decompositions) across a number of
different BLAS libraries as well as a GPU implementation. . To do so, it
takes advantage of the ability to 'plug and play' different BLAS
implementations easily on a Debian and/or Ubuntu system.  The current
version supports - reference blas (refblas) which are unaccelerated as a
baseline - Atlas which are tuned but typically configure single-threaded -
Atlas39 which are tuned and configured for multi-threaded mode - Goto Blas
which are accelerated and multithreaded - Intel MKL which are a commercial
accelerated and multithreaded version. As for GPU computing, we use the
CRAN package - gputools . For Goto Blas, the gotoblas2-helper script from
the ISM in Tokyo can be used. For Intel MKL we use the Revolution R
packages from Ubuntu 9.10.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.4-1
- initial package for Fedora