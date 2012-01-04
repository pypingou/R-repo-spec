%global packname  colbycol
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          Read big text files column by column, sometimes much bigger than available RAM, into R.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava R-filehash 

BuildRequires:    R-devel tex(latex) R-rJava R-filehash 

%description
This package tries to solve the memory restrictions posed by large text
files by breaking them into their columns first. These columns are later
read individually into R. The package also provides some helper functions
for manipulating the newly created objects.

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
%doc %{rlibdir}/colbycol/html
%doc %{rlibdir}/colbycol/DESCRIPTION
%{rlibdir}/colbycol/Meta
%{rlibdir}/colbycol/java
%{rlibdir}/colbycol/java_src
%{rlibdir}/colbycol/data
%{rlibdir}/colbycol/R
%{rlibdir}/colbycol/NAMESPACE
%{rlibdir}/colbycol/help
%{rlibdir}/colbycol/extdata
%{rlibdir}/colbycol/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7-1
- initial package for Fedora