%global packname  gstudio
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          GeneticStudio packages for R.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-MASS R-igraph 

BuildRequires:    R-devel tex(latex) R-methods R-MASS R-igraph 

%description
This package was created to support population genetics and landscape
genetic courses I teach at Virginia Commonwealth University.  This package
contains classes and functions for the analysis of marker data to include
structure statistics, analyses based upon allele frequencies, and the
Population Graphs network analysis of spatial conditional genetic

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora