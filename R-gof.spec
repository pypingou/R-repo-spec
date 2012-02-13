%global packname  gof
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.0
Release:          1%{dist}
Summary:          Model-diagnostics based on cumulative residuals

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Implementation of model-checking technique based on cumulative residuals

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
%doc %{rlibdir}/gof/CITATION
%doc %{rlibdir}/gof/DESCRIPTION
%doc %{rlibdir}/gof/html
%{rlibdir}/gof/demo
%{rlibdir}/gof/data
%{rlibdir}/gof/R
%{rlibdir}/gof/NAMESPACE
%{rlibdir}/gof/INDEX
%{rlibdir}/gof/Meta
%{rlibdir}/gof/libs
%{rlibdir}/gof/help

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.0-1
- Update to version 0.8.0

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.0-1
- initial package for Fedora