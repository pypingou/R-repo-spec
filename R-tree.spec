%global packname  tree
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.29
Release:          1%{?dist}
Summary:          Classification and regression trees

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-29.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grDevices R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-grDevices R-graphics R-stats 

%description
Classification and Regression Trees.

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
%doc %{rlibdir}/tree/LICENCE
%doc %{rlibdir}/tree/html
%doc %{rlibdir}/tree/DESCRIPTION
%{rlibdir}/tree/po
%{rlibdir}/tree/R
%{rlibdir}/tree/NAMESPACE
%{rlibdir}/tree/INDEX
%{rlibdir}/tree/help
%{rlibdir}/tree/libs
%{rlibdir}/tree/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.29-1
- initial package for Fedora