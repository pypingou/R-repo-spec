%global packname  dplR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Dendrochronology Program Library in R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-digest R-grid R-lattice R-XML 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-digest R-grid R-lattice R-XML 


%description
This package contains functions for performing tree-ring analyses, IO, and

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
%doc %{rlibdir}/dplR/html
%doc %{rlibdir}/dplR/DESCRIPTION
%doc %{rlibdir}/dplR/CITATION
%{rlibdir}/dplR/R
%{rlibdir}/dplR/help
%{rlibdir}/dplR/INDEX
%{rlibdir}/dplR/unitTests
%{rlibdir}/dplR/libs
%{rlibdir}/dplR/data
%{rlibdir}/dplR/NAMESPACE
%{rlibdir}/dplR/po
%{rlibdir}/dplR/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora