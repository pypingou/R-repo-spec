%global packname  RFA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.9
Release:          1%{?dist}
Summary:          Regional Frequency Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
Several function to perform a Regional Frequency Analysis

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
%doc %{rlibdir}/RFA/html
%doc %{rlibdir}/RFA/DESCRIPTION
%{rlibdir}/RFA/libs
%{rlibdir}/RFA/data
%{rlibdir}/RFA/Meta
%{rlibdir}/RFA/NAMESPACE
%{rlibdir}/RFA/INDEX
%{rlibdir}/RFA/R
%{rlibdir}/RFA/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.9-1
- initial package for Fedora