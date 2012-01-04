%global packname  qmrparser
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Parser combinator in R

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Basic functions for building parsers, with an application to PC-AXIS
format files.

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
%doc %{rlibdir}/qmrparser/html
%doc %{rlibdir}/qmrparser/DESCRIPTION
%doc %{rlibdir}/qmrparser/doc
%{rlibdir}/qmrparser/extdata
%{rlibdir}/qmrparser/help
%{rlibdir}/qmrparser/NAMESPACE
%{rlibdir}/qmrparser/INDEX
%{rlibdir}/qmrparser/noweb
%{rlibdir}/qmrparser/R
%{rlibdir}/qmrparser/Meta

%changelog
* Sun Dec 04 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora