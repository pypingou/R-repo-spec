%global packname  drawExpression
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Visualising R syntax through graphics

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grid 

BuildRequires:    R-devel tex(latex) R-grid 

%description
Graphical display of R expression, showing the interpretation of an
expression by R and the various kind of R data structure. The steps of the
interpretation of an expression are obtained through the parsed tree.

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
%doc %{rlibdir}/drawExpression/html
%doc %{rlibdir}/drawExpression/DESCRIPTION
%{rlibdir}/drawExpression/help
%{rlibdir}/drawExpression/NAMESPACE
%{rlibdir}/drawExpression/R
%{rlibdir}/drawExpression/INDEX
%{rlibdir}/drawExpression/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora