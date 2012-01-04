%global packname  seqCBS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          CN Profiling using Sequencing and CBS

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-clue 

BuildRequires:    R-devel tex(latex) R-clue 

%description
This is a method for DNA Copy Number Profiling using Next-Generation
Sequencing. It has new model and test statistics based on non-homogeneous
Poisson Processes with change point models. It uses an adaptation of
Circular Binary Segmentation. Also included are methods for point-wise
Bayesian Confidence Interval and model selection method for the
change-point model. A case and a control sample reads (normal and tumor)
are required.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora