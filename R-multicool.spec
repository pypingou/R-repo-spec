%global packname  multicool
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Permutations of multisets in cool-lex order.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A set of tools to permute multisets without loops or hash tables. The
package is based on C code from Aaron Williams. Cool-lex order is similar
to colexicographical order. The algorithm is described in Williams, A.
Loopless Generation of Multiset Permutations by Prefix Shifts. SODA 2009,
Symposium on Discrete Algorithms, New York, United States.

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
%doc %{rlibdir}/multicool/DESCRIPTION
%doc %{rlibdir}/multicool/html
%{rlibdir}/multicool/help
%{rlibdir}/multicool/Meta
%{rlibdir}/multicool/libs
%{rlibdir}/multicool/NAMESPACE
%{rlibdir}/multicool/R
%{rlibdir}/multicool/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora