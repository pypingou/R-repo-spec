%global packname  BACCO
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.4
Release:          1%{?dist}
Summary:          Bayesian Analysis of Computer Code Output (BACCO)

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-emulator R-calibrator R-approximator 

BuildRequires:    R-devel tex(latex) R-emulator R-calibrator R-approximator 

%description
The BACCO bundle of packages is replaced by the BACCO package, which
provides a vignette that illustrates the constituent packages (emulator,
approximator, calibrator) in use.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.4-1
- initial package for Fedora