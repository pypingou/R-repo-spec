%global packname  SoDA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Functions and Exampels for "Software for Data Analysis"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics 

BuildRequires:    R-devel tex(latex) R-methods R-graphics 

%description
Functions, examples and other software related to  the book "Software for
Data Analysis: Programming with R". See package?SoDA for  an  overview.

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
%doc %{rlibdir}/SoDA/doc
%doc %{rlibdir}/SoDA/DESCRIPTION
%doc %{rlibdir}/SoDA/html
%{rlibdir}/SoDA/R
%{rlibdir}/SoDA/demo
%{rlibdir}/SoDA/libs
%{rlibdir}/SoDA/Meta
%{rlibdir}/SoDA/NAMESPACE
%{rlibdir}/SoDA/Examples
%{rlibdir}/SoDA/data
%{rlibdir}/SoDA/testdata
%{rlibdir}/SoDA/exec
%{rlibdir}/SoDA/examplePages.csv
%{rlibdir}/SoDA/help
%{rlibdir}/SoDA/INDEX
%{rlibdir}/SoDA/LICENSE
%{rlibdir}/SoDA/Perl

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora