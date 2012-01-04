%global packname  agricolae
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.9
Release:          1%{?dist}
Summary:          Statistical Procedures for Agricultural Research

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Agricolae was presented on 28 August 2009 in the thesis "A statistical
analysis tool for agricultural research" to obtain the degree of Master on
science, mention Systems Engineering, of the facultad de ingenieria
industrial y de sistemas - Universidad Nacional de Ingenieria, Lima-Peru
(UNI), being approved with the qualification of 18.14 in a scale from 0 to
20. The thesis includes a satisfaction survey of the library, with an
index quality of the software of 0.8 in scale of 0-1. These functions are
currently used by the International Potato Center (CIP), the Universidad
Nacional Agraria La Molina (UNALM-PERU), and the Instituto Nacional de
Innovacion Agraria (INIA-PERU). It comprises the functionality of
statistical analysis into experimental designs applied specially in field
experiments in agriculture and plant breeding: Lattice, factorial,
complete and incomplete block, Latin Square, Graeco, Alpha designs,
Cyclic, augmented block, split and strip plot designs, comparison of
multi-location trials, comparison between treatments, resampling,
simulation, biodiversity indexes and consensus cluster.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.9-1
- initial package for Fedora