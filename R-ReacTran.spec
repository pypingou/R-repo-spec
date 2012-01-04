%global packname  ReacTran
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Reactive transport modelling in 1D, 2D and 3D

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rootSolve R-deSolve R-shape 

BuildRequires:    R-devel tex(latex) R-rootSolve R-deSolve R-shape 

%description
Routines for developing models that describe reaction and
advective-diffusive transport in one, two or three dimensions. Includes
transport routines in porous media, in estuaries, and in bodies with
variable shape.

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
%doc %{rlibdir}/ReacTran/NEWS
%doc %{rlibdir}/ReacTran/html
%doc %{rlibdir}/ReacTran/DESCRIPTION
%doc %{rlibdir}/ReacTran/doc
%{rlibdir}/ReacTran/NAMESPACE
%{rlibdir}/ReacTran/libs
%{rlibdir}/ReacTran/Meta
%{rlibdir}/ReacTran/INDEX
%{rlibdir}/ReacTran/R
%{rlibdir}/ReacTran/help
%{rlibdir}/ReacTran/demo

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.2-1
- initial package for Fedora