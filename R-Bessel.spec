%global packname  Bessel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Bessel -- Bessel Functions Computations and Approximations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rmpfr 


BuildRequires:    R-devel tex(latex) R-Rmpfr



%description
Bessel Function Computations for complex and real numbers; notably
interfacing TOMS 644; approximations for large arguments, experiments,

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.3-1
- initial package for Fedora