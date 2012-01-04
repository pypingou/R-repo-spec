%global packname  exact2x2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1.0
Release:          1%{?dist}
Summary:          Exact Conditional Tests and Confidence Intervals for 2x2 tables

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-exactci 

BuildRequires:    R-devel tex(latex) R-stats R-exactci 

%description
Calculates Fisher's exact test, Blaker's exact test, or the exact
McNemar's test with appropriate matching confidence intervals.

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
%doc %{rlibdir}/exact2x2/CITATION
%doc %{rlibdir}/exact2x2/html
%doc %{rlibdir}/exact2x2/doc
%doc %{rlibdir}/exact2x2/DESCRIPTION
%{rlibdir}/exact2x2/Meta
%{rlibdir}/exact2x2/INDEX
%{rlibdir}/exact2x2/R
%{rlibdir}/exact2x2/NAMESPACE
%{rlibdir}/exact2x2/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1.0-1
- initial package for Fedora