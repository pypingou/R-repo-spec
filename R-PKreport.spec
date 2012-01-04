%global packname  PKreport
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          A reporting pipeline for checking population pharmacokinetic model assumption

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-lattice R-ggplot2 

BuildRequires:    R-devel tex(latex) R-methods R-lattice R-ggplot2 

%description
PKreport aims to 1) provide automatic pipeline for users to visualize data
and models. It creates a flexible R framework with automatically generated
R scripts to save time and cost for later usage; 2) implement an
archive-oriented management tool for users to store, retrieve and modify
figures. 3) offer powerful and convenient service to generate high-quality
graphs based on two R packages: lattice and ggplot2.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora