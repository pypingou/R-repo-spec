%global packname  Brobdingnag
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Very large numbers in R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics 

BuildRequires:    R-devel tex(latex) R-methods R-graphics 

%description
Handles very large numbers in R.  Real numbers are held using their
natural logarithms, plus a logical flag indicating sign.  The package
includes a vignette that gives a step-by-step introduction to using S4

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora