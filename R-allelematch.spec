%global packname  allelematch
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Identification of unique multilocus genotypes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-dynamicTreeCut 

BuildRequires:    R-devel tex(latex) R-dynamicTreeCut 

%description
This package provides tools for the identification of unique of multilocus
genotypes when both genotyping error and missing data are present. The
package is targeted at those working with large datasets and databases
containing multiple samples of each individual, a situation that is common
in conservation genetics, and particularly in non-invasive wildlife
sampling applications. Functions explicitly incorporate missing data, and
can tolerate allele mismatches created by genotyping error.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora