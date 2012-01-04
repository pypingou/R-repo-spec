%global packname  timecourse
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Statistical Analysis for Developmental Microarray Time Course Data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-methods 
Requires:         R-Biobase R-graphics R-limma R-MASS R-marray R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-MASS R-methods
BuildRequires:    R-Biobase R-graphics R-limma R-MASS R-marray R-methods R-stats 


%description
Functions for data analysis and graphical displays for developmental
microarray time course data.

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
%doc %{rlibdir}/timecourse/doc
%doc %{rlibdir}/timecourse/DESCRIPTION
%doc %{rlibdir}/timecourse/html
%{rlibdir}/timecourse/data
%{rlibdir}/timecourse/R
%{rlibdir}/timecourse/INDEX
%{rlibdir}/timecourse/help
%{rlibdir}/timecourse/NAMESPACE
%{rlibdir}/timecourse/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora