%global packname  spuRs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Functions and Datasets for "Introduction to Scientific Programming and Simulation Using R".

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-lattice 

BuildRequires:    R-devel tex(latex) R-MASS R-lattice 

%description
This package provides functions and datasets from the book "Introduction
to Scientific Programming and Simulation Using R".

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
%doc %{rlibdir}/spuRs/html
%doc %{rlibdir}/spuRs/DESCRIPTION
%{rlibdir}/spuRs/Meta
%{rlibdir}/spuRs/resources
%{rlibdir}/spuRs/NAMESPACE
RPM build errors:
%{rlibdir}/spuRs/help
%{rlibdir}/spuRs/data
%{rlibdir}/spuRs/INDEX
%{rlibdir}/spuRs/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora