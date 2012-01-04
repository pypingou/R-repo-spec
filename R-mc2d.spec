%global packname  mc2d
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.12
Release:          1%{?dist}
Summary:          Tools for Two-Dimensional Monte-Carlo Simulations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Various distributions and utilities to ease the use of R to build and
study Two-Dimensional Monte-Carlo simulations

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
%doc %{rlibdir}/mc2d/CITATION
%doc %{rlibdir}/mc2d/doc
%doc %{rlibdir}/mc2d/DESCRIPTION
%doc %{rlibdir}/mc2d/html
%doc %{rlibdir}/mc2d/NEWS
%{rlibdir}/mc2d/help
%{rlibdir}/mc2d/INDEX
%{rlibdir}/mc2d/Meta
%{rlibdir}/mc2d/data
%{rlibdir}/mc2d/R
%{rlibdir}/mc2d/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.12-1
- initial package for Fedora