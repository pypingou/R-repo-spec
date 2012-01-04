%global packname  SciViews
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.4
Release:          1%{?dist}
Summary:          SciViews GUI API - Main package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-grDevices R-graphics R-MASS 
Requires:         R-ellipse 

BuildRequires:    R-devel tex(latex) R-stats R-grDevices R-graphics R-MASS
BuildRequires:    R-ellipse 


%description
Functions to install SciViews additions to R, and more (various) tools

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
%doc %{rlibdir}/SciViews/NEWS
%doc %{rlibdir}/SciViews/CITATION
%doc %{rlibdir}/SciViews/html
%doc %{rlibdir}/SciViews/doc
%doc %{rlibdir}/SciViews/DESCRIPTION
%{rlibdir}/SciViews/Meta
%{rlibdir}/SciViews/LICENSE
%{rlibdir}/SciViews/INDEX
%{rlibdir}/SciViews/NAMESPACE
%{rlibdir}/SciViews/help
%{rlibdir}/SciViews/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.4-1
- initial package for Fedora