%global packname  IPSUR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Introduction to Probability and Statistics Using R

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains the Sweave source code used to generate IPSUR, an
introductory probability and statistics textbook, alongside other
supplementary materials such as the parsed R code for the book and data
for the examples and exercises.  The book is released under the GNU Free
Documentation License.

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
%doc %{rlibdir}/IPSUR/doc
%doc %{rlibdir}/IPSUR/DESCRIPTION
%doc %{rlibdir}/IPSUR/html
%{rlibdir}/IPSUR/Meta
%{rlibdir}/IPSUR/LICENSE
%{rlibdir}/IPSUR/NAMESPACE
%{rlibdir}/IPSUR/IPSUR.R
%{rlibdir}/IPSUR/help
%{rlibdir}/IPSUR/INDEX
%{rlibdir}/IPSUR/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora