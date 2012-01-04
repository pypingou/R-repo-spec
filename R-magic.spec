%global packname  magic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.6
Release:          1%{?dist}
Summary:          create and investigate magic squares

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-abind 

BuildRequires:    R-devel tex(latex) R-abind 

%description
a collection of efficient, vectorized algorithms for the creation and
investigation of magic squares and hypercubes, including a variety of
functions for the manipulation and analysis of arbitrarily dimensioned
arrays.  The package includes methods for creating normal magic squares of
any order greater than 2.  The ultimate intention is for the package to be
a computerized embodiment all magic square knowledge, including direct
numerical verification of properties of magic squares (such as recent
results on the determinant of odd-ordered semimagic squares).  Some
antimagic functionality is included.  The package also serves as a
rebuttal to the often-heard comment "I thought R was just for statistics".

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.6-1
- initial package for Fedora