%global packname  nlstools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.11
Release:          1%{?dist}
Summary:          Tools for nonlinear regression diagnostics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Several tools for assessing the quality of fit of a gaussian nonlinear
model are provided.

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
%doc %{rlibdir}/nlstools/NEWS
%doc %{rlibdir}/nlstools/html
%doc %{rlibdir}/nlstools/doc
%doc %{rlibdir}/nlstools/DESCRIPTION
%doc %{rlibdir}/nlstools/CITATION
%doc %{rlibdir}/nlstools/LICENCE
%{rlibdir}/nlstools/data
%{rlibdir}/nlstools/gpl-3.0.txt
%{rlibdir}/nlstools/R
%{rlibdir}/nlstools/NAMESPACE
%{rlibdir}/nlstools/Meta
%{rlibdir}/nlstools/help
%{rlibdir}/nlstools/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.11-1
- initial package for Fedora