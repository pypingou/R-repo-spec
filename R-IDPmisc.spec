%global packname  IDPmisc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.16
Release:          1%{?dist}
Summary:          Utilities of Institute of Data Analyses and Process Design (www.idp.zhaw.ch)

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-grid R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-grid R-lattice 

%description
The IDPmisc package contains different high-level graphics functions for
displaying large datasets, displaying circular data in a very flexible
way, finding local maxima, brewing color ramps, drawing nice arrows,
zooming 2D-plots, creating figures with differently colored margin and
plot region.  In addition, the package contains auxiliary functions for
data manipulation like omitting observations with irregular values or
selecting data by logical vectors, which include NAs. Other functions are
especially useful in spectroscopy and analyses of environmental data:
robust baseline fitting, finding peaks in spectra.

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
%doc %{rlibdir}/IDPmisc/DESCRIPTION
%doc %{rlibdir}/IDPmisc/html
%{rlibdir}/IDPmisc/R
%{rlibdir}/IDPmisc/NAMESPACE
%{rlibdir}/IDPmisc/INDEX
%{rlibdir}/IDPmisc/help
%{rlibdir}/IDPmisc/data
%{rlibdir}/IDPmisc/libs
%{rlibdir}/IDPmisc/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.16-1
- initial package for Fedora