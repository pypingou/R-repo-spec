%global packname  ptw
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Parametric Time Warping

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Parametric Time Warping aligns patterns, i.e. it aims to put corresponding
features at the same locations. The algorithm searches for an optimal
polynomial describing the warping. It is possible to align one sample to a
reference, several samples to the same reference, or several samples to
several references. One can choose between calculating individual
warpings, or one global warping for a set of samples and one reference.
Two optimization criteria are implemented: RMS (Root Mean Square error)
and WCC (Weighted Cross Correlation).

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
%doc %{rlibdir}/ptw/DESCRIPTION
%doc %{rlibdir}/ptw/CITATION
%doc %{rlibdir}/ptw/html
%{rlibdir}/ptw/libs
%{rlibdir}/ptw/demo
%{rlibdir}/ptw/Meta
%{rlibdir}/ptw/NAMESPACE
%{rlibdir}/ptw/R
%{rlibdir}/ptw/help
%{rlibdir}/ptw/data
%{rlibdir}/ptw/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora