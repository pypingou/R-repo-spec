%global packname  MPTinR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.5
Release:          1%{?dist}
Summary:          Analyze Multinomial Processing Tree Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package provides a user-friendly way for analysis of multinomial
processing tree (MPT) models (e.g.,  Riefer, D. M., and Batchelder, W. H.
[1988]. Multinomial modeling and the measurement of cognitive processes.
Psychological Review, 95, 318-339) for individual and multi-individual
data. The main functions perform model fitting and model selection. Model
selection can be done using e.g. the minimum description length measure
based on the Fischer information approximation (FIA). The FIA can be
obtained for any MPT model using the algorithm provided by Wu, Myung, &
Batchelder (2010, JMP) ported to R. The model and restrictions can easily
be specified in external files. The 'classical' .EQN file format for model
files is also supported. Furthermore, MPTinR supports multicore fitting
using the snowfall package.

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
%doc %{rlibdir}/MPTinR/NEWS
%doc %{rlibdir}/MPTinR/html
%doc %{rlibdir}/MPTinR/DESCRIPTION
%{rlibdir}/MPTinR/Meta
%{rlibdir}/MPTinR/data
%{rlibdir}/MPTinR/NAMESPACE
%{rlibdir}/MPTinR/R
%{rlibdir}/MPTinR/extdata
%{rlibdir}/MPTinR/INDEX
%{rlibdir}/MPTinR/help

%changelog
* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.5-1
- initial package for Fedora