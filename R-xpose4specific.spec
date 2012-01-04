%global packname  xpose4specific
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.3.2
Release:          1%{?dist}
Summary:          Xpose 4 Specific Functions Package

Group:            Applications/Engineering 
License:          LGPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-grid R-Hmisc R-gam R-methods R-xpose4data R-xpose4generic 

BuildRequires:    R-devel tex(latex) R-lattice R-grid R-Hmisc R-gam R-methods R-xpose4data R-xpose4generic 

%description
Xpose is collection of packages to be used as a model building aid for
non-linear mixed effects (population) analysis using NONMEM. It
facilitates data set checkout, exploration and visualization, model
diagnostics, candidate covariate identification and model comparison.
Xpose4specific is a package containing specific plotting functions, which
require relatively little user input, but are less customizable than the
plot commands found in xpose4generic.

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
%doc %{rlibdir}/xpose4specific/DESCRIPTION
%doc %{rlibdir}/xpose4specific/html
%doc %{rlibdir}/xpose4specific/CITATION
%{rlibdir}/xpose4specific/Meta
%{rlibdir}/xpose4specific/readme.txt
%{rlibdir}/xpose4specific/R
%{rlibdir}/xpose4specific/INDEX
%{rlibdir}/xpose4specific/help
%{rlibdir}/xpose4specific/changelog.txt
%{rlibdir}/xpose4specific/NAMESPACE

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.3.2-1
- initial package for Fedora