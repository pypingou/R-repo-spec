%global packname  HSAUR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          A Handbook of Statistical Analyses Using R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-MASS R-scatterplot3d 


BuildRequires:    R-devel tex(latex) R-lattice R-MASS R-scatterplot3d



%description
Functions, data sets, analyses and examples from the book `A Handbook of
Statistical Analyses Using R' (Brian S. Everitt and Torsten Hothorn,
Chapman & Hall/CRC, 2006). The first chapter of the book, which is
entitled `An Introduction to R', is completely included in this package,
for all other chapters, a vignette containing all data analyses is

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
%doc %{rlibdir}/HSAUR/doc
%doc %{rlibdir}/HSAUR/DESCRIPTION
%doc %{rlibdir}/HSAUR/html
%{rlibdir}/HSAUR/cache
%{rlibdir}/HSAUR/NAMESPACE
%{rlibdir}/HSAUR/rawdata
%{rlibdir}/HSAUR/data
RPM build errors:
%{rlibdir}/HSAUR/R
%{rlibdir}/HSAUR/Meta
%{rlibdir}/HSAUR/help
%{rlibdir}/HSAUR/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora