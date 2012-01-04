%global packname  BB
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.8.1
Release:          1%{?dist}
Summary:          Solving and Optimizing Large-Scale Nonlinear Systems

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-quadprog 

BuildRequires:    R-devel tex(latex) R-quadprog 

%description
Barzilai-Borwein spectral methods for solving nonlinear system of
equations, and for optimizing nonlinear objective functions subject to
simple constraints. A tutorial style introduction to this package is
available in a vignette on the CRAN download page or, when the package is
loaded in an R session, with vignette("BB").

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.8.1-1
- initial package for Fedora