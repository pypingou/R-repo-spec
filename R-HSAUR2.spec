%global packname  HSAUR2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          A Handbook of Statistical Analyses Using R (2nd Edition)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-MASS R-scatterplot3d 

BuildRequires:    R-devel tex(latex) R-lattice R-MASS R-scatterplot3d 

%description
Functions, data sets, analyses and examples from the second edition of the
book `A Handbook of Statistical Analyses Using R' (Brian S. Everitt and
Torsten Hothorn, Chapman & Hall/CRC, 2008). The first chapter of the book,
which is entitled `An Introduction to R', is completely included in this
package, for all other chapters, a vignette containing all data analyses
is available.

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
%doc %{rlibdir}/HSAUR2/DESCRIPTION
%doc %{rlibdir}/HSAUR2/html
%doc %{rlibdir}/HSAUR2/doc
%{rlibdir}/HSAUR2/Meta
%{rlibdir}/HSAUR2/INDEX
%{rlibdir}/HSAUR2/help
%{rlibdir}/HSAUR2/cache
%{rlibdir}/HSAUR2/NAMESPACE
%{rlibdir}/HSAUR2/R
RPM build errors:
%{rlibdir}/HSAUR2/rawdata
%{rlibdir}/HSAUR2/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora