%global packname  smacof
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          SMACOF for Multidimensional Scaling.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-polynom R-rgl R-scatterplot3d R-Hmisc R-colorspace 
Requires:         R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-polynom R-rgl R-scatterplot3d R-Hmisc R-colorspace
BuildRequires:    R-graphics R-stats 


%description
This package provides the following approaches of multidimensional scaling
(MDS) based on stress minimization by means of majorization (smacof):
Simple smacof on symmetric dissimilarity matrices, smacof for rectangular
matrices (unfolding models), smacof with constraints on the configuration,
three-way smacof for individual differences (including constraints for
idioscal, indscal, and identity), and spherical smacof (primal and dual
algorithm). Each of these approaches is implemented in a metric and
nonmetric manner including primary, secondary, and tertiary approaches for
tie handling. Jackknife and permutation tests are included as well.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora