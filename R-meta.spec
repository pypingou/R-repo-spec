%global packname  meta
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.1
Release:          1%{?dist}
Summary:          Meta-Analysis with R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grid 

BuildRequires:    R-devel tex(latex) R-grid 

%description
Fixed and random effects meta-analysis. Functions for tests of bias,
forest and funnel plot.

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
%doc %{rlibdir}/meta/DESCRIPTION
%doc %{rlibdir}/meta/NEWS
%doc %{rlibdir}/meta/html
%{rlibdir}/meta/help
%{rlibdir}/meta/INDEX
%{rlibdir}/meta/Meta
%{rlibdir}/meta/NAMESPACE
%{rlibdir}/meta/libs
%{rlibdir}/meta/R
%{rlibdir}/meta/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.1-1
- initial package for Fedora