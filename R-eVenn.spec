%global packname  eVenn
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.4
Release:          1%{?dist}
Summary:          eVenn: A powerful tool to compare lists and draw Venn diagrams.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
Compute a matrix comparison of lists (from 2 to infinite) and plot the
results in a Venn diagram if (N<=4) with regulation details. It allows to
produce a complete annotated file, merging the annotations of the compared
lists. It is also possible to compute an overlaps table to show the
overlaps proportions of all the couples of lists and draw proportional
Venn diagrams.

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
%doc %{rlibdir}/eVenn/html
%doc %{rlibdir}/eVenn/DESCRIPTION
%{rlibdir}/eVenn/INDEX
%{rlibdir}/eVenn/help
%{rlibdir}/eVenn/data
%{rlibdir}/eVenn/Meta
%{rlibdir}/eVenn/NAMESPACE
%{rlibdir}/eVenn/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.4-1
- initial package for Fedora