%global packname  DEDS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Differential Expression via Distance Summary for Microarray Data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This library contains functions that calculate various statistics of
differential expression for microarray data, including t statistics, fold
change, F statistics, SAM, moderated t and F statistics and B statistics.
It also implements a new methodology called DEDS (Differential Expression
via Distance Summary), which selects differentially expressed genes by
integrating and summarizing a set of statistics using a weighted distance

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
%doc %{rlibdir}/DEDS/doc
%doc %{rlibdir}/DEDS/html
%doc %{rlibdir}/DEDS/DESCRIPTION
%{rlibdir}/DEDS/libs
%{rlibdir}/DEDS/Meta
%{rlibdir}/DEDS/data
%{rlibdir}/DEDS/R
%{rlibdir}/DEDS/NAMESPACE
%{rlibdir}/DEDS/help
%{rlibdir}/DEDS/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora