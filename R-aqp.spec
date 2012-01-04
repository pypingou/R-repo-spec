%global packname  aqp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.99.8.47
Release:          1%{?dist}
Summary:          Algorithms for Quantitative Pedology

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.99-8.47.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-plyr R-reshape R-lattice R-grid R-cluster R-sp R-Hmisc R-stringr 


BuildRequires:    R-devel tex(latex) R-methods R-plyr R-reshape R-lattice R-grid R-cluster R-sp R-Hmisc R-stringr



%description
A collection of algorithms related to modeling of soil resources, soil
classification, soil profile aggregation, and visualization.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.8.47-1
- initial package for Fedora