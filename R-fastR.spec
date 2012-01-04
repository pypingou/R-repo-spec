%global packname  fastR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.14
Release:          1%{?dist}
Summary:          Data sets and utilities for Foundations and Applications of Statistics by R Pruim

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-grid R-mosaic 


BuildRequires:    R-devel tex(latex) R-lattice R-grid R-mosaic



%description
Data sets and utilities for Foundations and Applications of Statistics:an
Introduction using R by R Pruim

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
%doc %{rlibdir}/fastR/DESCRIPTION
%doc %{rlibdir}/fastR/html
%{rlibdir}/fastR/R
%{rlibdir}/fastR/snippet
%{rlibdir}/fastR/help
%{rlibdir}/fastR/INDEX
%{rlibdir}/fastR/data
%{rlibdir}/fastR/Meta
%{rlibdir}/fastR/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.14-1
- initial package for Fedora