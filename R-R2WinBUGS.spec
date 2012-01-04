%global packname  R2WinBUGS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.18
Release:          1%{?dist}
Summary:          Running WinBUGS and OpenBUGS from R / S-PLUS

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-18.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-coda 

BuildRequires:    R-devel tex(latex) R-coda 

%description
Using this package, it is possible to call a BUGS model, summarize
inferences and convergence in a table and graph, and save the simulations
in arrays for easy access in R / S-PLUS. In S-PLUS, the openbugs
functionality and the windows emulation functionality is not yet

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.18-1
- initial package for Fedora